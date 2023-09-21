/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/20 18:51:49 by wberger           #+#    #+#             */
/*   Updated: 2022/07/20 19:17:45 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
int	ft_ultimate_range(int **range, int min, int max)
{
	int	i;
	int	size;
	int	*tab;

	i = 0;
	size = max - min;
	if (size < 0 || size == 0)
	{
		return (0);
	}
	tab = malloc(sizeof(*tab) * size);
	if (!tab)
		return (0);
	while (max != min)
	{
		tab[i++] = min++;
	}
	range = &tab;
	return (i);
}
